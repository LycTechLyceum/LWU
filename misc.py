from app_config import CODES_PATH


def check_code(code):
    with open(CODES_PATH) as file:
        admin_code = file.readline().replace("\n", "")
        print(admin_code)
        executor_code = file.readline()
        print(executor_code)
        if admin_code == code:
            return "Admin"
        elif executor_code == code:
            return "Executor"
        else:
            return "no"
