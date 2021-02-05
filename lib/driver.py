import config
import os
import shutil
import stat
from selenium import webdriver
# from fake_useragent import UserAgent


class Driver:
    setupFlag = False
    chromiumPath = ""
    driverPath = ""

    def setup(event):
        if Driver.setupFlag is False:
            chromiumBinPath = os.path.join(config.binDir, config.chromiumBin)
            driverBinPath = os.path.join(config.binDir, config.driverBin)
            if event:
                # event exitsts: Run on Cloud Functions
                chromiumTmpPath = os.path.join(config.tmpDir, config.chromiumBin)
                driverTmpPath = os.path.join(config.tmpDir, config.driverBin)
                shutil.copyfile(chromiumBinPath, chromiumTmpPath)
                shutil.copyfile(driverBinPath, driverTmpPath)
                os.chmod(chromiumTmpPath, stat.S_IWUSR)
                os.chmod(chromiumTmpPath, stat.S_IWGRP)
                os.chmod(driverTmpPath, stat.S_IWUSR)
                os.chmod(driverTmpPath, stat.S_IWGRP)
                Driver.chromiumPath = chromiumTmpPath
                Driver.driverPath = driverTmpPath
            else:
                # event empty: Run on local
                Driver.chromiumPath = chromiumBinPath
                Driver.driverPath = driverBinPath
            Driver.setupFlag = True

    def new():
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1280x1696')
        options.add_argument('--no-sandbox')
        options.add_argument('--hide-scrollbars')
        options.add_argument('--lang=ja-JP')
        options.add_argument('--enable-logging')
        options.add_argument('--log-level=0')
        options.add_argument('--v=99')
        options.add_argument('--single-process')
        options.add_argument('--ignore-certificate-errors')
        # options.add_argument('user-agent=' + UserAgent().random)
        options.binary_location = Driver.chromiumPath
        return webdriver.Chrome(Driver.driverPath, options=options)
