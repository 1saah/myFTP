import os.path
import sys

path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path)

if __name__ == "__main__":
    from core import management
    manage = management.management_tool(sys.argv)
    manage.check()
    manage.execute()



