import pytest
import sys

@pytest.mark.usefixtures('driver')
class TestLink:
	def test_download():
		"""
		Verify download
		:return: None
		"""
		driver.get('https://chromedriver.storage.googleapis.com/index.html?path=79.0.3945.36/')
		driver.maximize_window()
		sleep(2)
		driver.find_element_by_xpath("/html/body/table/tbody/tr[]/td[2]/a").click()
		sleep(5)
		assert driver.execute_script("lambda-file-exists=chromedriver_win32.zip") == True
