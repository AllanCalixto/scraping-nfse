from driver import start_driver
from login import login_nfse
from flows import new_nfse, new_nfse_service

def main():
    driver = start_driver()

    driver = login_nfse(driver)
    driver = new_nfse(driver)
    driver = new_nfse_service(driver)

    input("Pressione Enter para fechar...")
    driver.quit()


if __name__ == "__main__":
    main()