import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class SauceDemoTests(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Khởi tạo trình duyệt (chạy 1 lần trước khi thực hiện các Testcase)
        service = Service(ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=service)
        cls.driver.maximize_window()
        # Đợi tối đa 5s nếu phần tử chưa load kịp (thay thế cho việc phải dùng sleep nhiều)
        cls.driver.implicitly_wait(5)

    def test_01_login(self):
        """Testcase 1: Đăng nhập"""
        self.driver.get("https://www.saucedemo.com/")
        
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        
        # Assert.assertTrue(driver.getCurrentUrl().contains("inventory"));
        self.assertTrue("inventory" in self.driver.current_url)

    def test_02_add_to_cart(self):
        """Testcase 2: Thêm vào giỏ hàng"""
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        
        count = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        
        # Assert.assertEquals(count, "1");
        self.assertEqual(count, "1")

    def test_03_logout(self):
        """Testcase 3: Đăng xuất"""
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        
        # Thread.sleep(1000);
        time.sleep(1)
        
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        
        # Assert.assertTrue(driver.getCurrentUrl().contains("saucedemo"));
        self.assertTrue("saucedemo" in self.driver.current_url)

    @classmethod
    def tearDownClass(cls):
        # Đóng trình duyệt sau khi chạy xong toàn bộ Testcase
        time.sleep(2) # Dừng lại 2s để quan sát trước khi tắt
        cls.driver.quit()

if __name__ == "__main__":
    # Lệnh này giúp chạy các testcase khi thực thi file
    unittest.main(verbosity=2)
