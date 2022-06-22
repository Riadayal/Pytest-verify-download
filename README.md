# How to verify file download in automation test in Pytest on [LambdaTest](https://www.lambdatest.com/?utm_source=github&utm_medium=repo&utm_campaign=Pytest-verify-download)

If you want to verify file download in automation test in Pytest on LambdaTest, you can follow the below steps. You can refer to sample test repo [here](https://github.com/LambdaTest/Pytest-Selenium-sample).

# Steps:


## Step 1: Add test case

You can use the following testcase and save it as `verify_download.py`:

```python
import pytest
import 	sys

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
```

## Step 2: Run your test

```bash
python verify_download.py
```

# Links:

[LambdaTest Community](http://community.lambdatest.com/)



