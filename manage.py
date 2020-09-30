from app import app
import unittest
import coverage
from flask_script import Manager

# Initializing the manager
manager = Manager(app)

# Test coverage configuration
COV = coverage.coverage(
    branch=True,
    include='app/*',
    omit=[
        'app/__init__.py',
    ]
)
COV.start()


# Add test command
@manager.command
def test():
    """
    Run tests without coverage
    :return:
    """
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


# Run the manager
if __name__ == '__main__':
    manager.run()
