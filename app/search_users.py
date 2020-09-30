import app.const as const
import requests
import geopandas as gpd
import pandas as pd
from shapely.geometry import Point
from app.helper import error_obj


def get_all_user_data():
    const.HTTP_ERROR = False
    r = requests.get(const.USER_API_URL + '/users')
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        const.HTTP_ERROR = True
        status_code = e.response.status_code
        message = e.response.reason
        return error_obj(message,status_code)
    r_obj = r.json()
    return r_obj


def get_user_data_by_live_place():
    const.HTTP_ERROR = False
    r = requests.get(const.USER_API_URL + '/city/users')
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        const.HTTP_ERROR = True
        status_code = e.response.status_code
        message = e.response.reason
        return error_obj(message,status_code)
    r_obj = r.json()
    return r_obj


def get_user_data_by_vicinity():
    all_user_data_result = get_all_user_data()
    if not const.HTTP_ERROR:
        # Set the area proximity geodataframe
        df_wgs84 = pd.DataFrame({'id': [1],
                                     'latitude': [1.23],
                                     'longitude': [-0.213]})
        df_wgs84_geom = [Point(xy) for xy in zip(df_wgs84.longitude, df_wgs84.latitude)]
        wgs84_crs = {'init': 'epsg:4326'}
        geo_df_wgs84 = gpd.GeoDataFrame(df_wgs84, crs=wgs84_crs, geometry=df_wgs84_geom)
        df_web_mercator = geo_df_wgs84.to_crs(epsg=3857)
        df_web_mercator['geometry'] = df_web_mercator.geometry.buffer(const.PROXIMITY)
        # Set the user data geodataframe
        all_user_df = pd.DataFrame.from_dict(all_user_data_result, orient='columns')
        all_user_df['longitude'] = pd.to_numeric(all_user_df['longitude'], downcast='float')
        all_user_df['latitude'] = pd.to_numeric(all_user_df['latitude'], downcast='float')
        all_user_geom = [Point(xy) for xy in zip(all_user_df.longitude, all_user_df.latitude)]
        all_user_geo_df = gpd.GeoDataFrame(all_user_df, crs=wgs84_crs, geometry=all_user_geom)
        all_user_geo_df_web_mercator = all_user_geo_df.to_crs(epsg=3857)
        # Overlay the user data geodataframe with the area proximity geodataframe to retrieve target users data
        target_users_gdf = gpd.overlay(all_user_geo_df_web_mercator,df_web_mercator, how='intersection')
        # Set the target users list
        target_users_id_list = []
        for index, row in target_users_gdf.iterrows():
            target_users_id_list.append(row['id_1'])
        target_users_item_list = []
        for user_item in all_user_data_result:
            if user_item['id'] in target_users_id_list:
                target_users_item_list.append(user_item)
        return target_users_item_list
    else:
        return all_user_data_result
