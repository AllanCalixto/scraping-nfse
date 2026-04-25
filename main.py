from driver import start_driver
from login import login_nfse
from flows import new_nfse

def main():
    driver = start_driver()

    driver = login_nfse(driver)
    driver = new_nfse(driver)

    input("Pressione Enter para fechar...")
    driver.quit()


if __name__ == "__main__":
    main()