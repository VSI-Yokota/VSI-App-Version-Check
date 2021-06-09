# coding: utf-8

from checkers.jpcert import JPCertCheck
from checkers.php import PHPVersionCheck
from checkers.php_for_win import PHP4WindowsVersionCheck
from checkers.apache import ApacheVersionCheck
from checkers.open_ssl import OpenSSLVersionCheck
from checkers.mysql import MySQL56VersionCheck
from checkers.mysql import MySQL57VersionCheck
from checkers.mysql import MySQL80VersionCheck
from checkers.wordpress import WordPressVersionCheck
from checkers.wordpress import WordPressJPVersionCheck
from checkers.wordpress_security import WordPressSecurityVersionCheck
from checkers.modx import MODXVersionCheck
from checkers.kusanagi import KusanagiVersionCheck
from checkers.firefox import FirefoxVersionCheck
from checkers.ios import IOSVersionCheck
from checkers.windows import WindowsVersionCheck
from checkers.chrome import ChromeVersionCheck
from checkers.acrobat import AcrobatVersionCheck
from checkers.creative_cloud import CreativeCloudVersionCheck
from checkers.android import AndroidVersionCheck
from checkers.aquos import AquosVersionCheck
from checkers.buffalo import TeraStationVersionCheck
from checkers.buffalo import WZR_D1100HVersionCheck
from checkers.yamaha import RTX1200VersionCheck
from checkers.yamaha import RTX1210VersionCheck
from checkers.yamaha import WXL202VersionCheck
from checkers.aterm_wg2600hp3 import AtermWG2600HP3VersionCheck
from checkers.cybozu import CybozuVersionCheck
from datetime import datetime, timedelta

checkers = (
    PHPVersionCheck("http://php.net/"),
    PHP4WindowsVersionCheck("http://windows.php.net/download/"),
    ApacheVersionCheck("http://httpd.apache.org/"),
    OpenSSLVersionCheck("https://www.openssl.org/"),
    MySQL56VersionCheck("https://dev.mysql.com/doc/relnotes/mysql/5.6/en/"),
    MySQL57VersionCheck("https://dev.mysql.com/doc/relnotes/mysql/5.7/en/"),
    MySQL80VersionCheck("https://dev.mysql.com/doc/relnotes/mysql/8.0/en/"),
    WordPressVersionCheck("https://wordpress.org/releases/"),
    WordPressJPVersionCheck("https://ja.wordpress.org/releases/"),
    WordPressSecurityVersionCheck("https://wordpress.org/news/category/security/"),
    MODXVersionCheck("http://modx.jp/news/"),
    KusanagiVersionCheck("https://kusanagi.tokyo/archives/"),
    FirefoxVersionCheck("https://www.mozilla.org/en-US/firefox/releases/"),
    IOSVersionCheck("https://support.apple.com/en-us/HT201222"),
    ChromeVersionCheck("https://chromereleases.googleblog.com/"),
    AcrobatVersionCheck("https://helpx.adobe.com/acrobat/release-note/release-notes-acrobat-reader.html"),
    CreativeCloudVersionCheck("https://helpx.adobe.com/creative-cloud/release-note/cc-release-notes.html"),
    AndroidVersionCheck("https://source.android.com/security/bulletin?hl=ja"),
    AquosVersionCheck("https://k-tai.sharp.co.jp/support/other/shm08/update/index.html"),
    TeraStationVersionCheck("http://buffalo.jp/download/driver/hd/ts5000_fw-win.html"),
    WZR_D1100HVersionCheck("https://www.buffalo.jp/support/download/detail/?dl_contents_id=61636"),
    RTX1200VersionCheck("http://www.rtpro.yamaha.co.jp/RT/docs/relnote/Rev.10.01/"),
    RTX1210VersionCheck("http://www.rtpro.yamaha.co.jp/RT/docs/relnote/Rev.14.01/"),
    WXL202VersionCheck("http://www.rtpro.yamaha.co.jp/RT/docs/relnote/ap/Rev.16.00/"),
    AtermWG2600HP3VersionCheck("https://www.aterm.jp/support/verup/wg2600hp3/fw.html"),
    CybozuVersionCheck("https://cs.cybozu.co.jp/office10/"),
    WindowsVersionCheck("https://portal.msrc.microsoft.com/ja-jp/security-guidance"),
    JPCertCheck("https://www.jpcert.or.jp/at/{}.html".format(datetime.now().year)),
)

def get_target_date():

    file = 'target_date'
    try:
        with open(file, mode='r') as f:
            str_date = f.read()
        
        with open(file, mode='w') as f:
            yesterday = datetime.today() - timedelta(days=1)
            f.write(yesterday.strftime('%Y-%m-%d'))

        return datetime.strptime(str_date, '%Y-%m-%d')

    except Exception as e:
        print(e)


if __name__ == '__main__':
    target_date = get_target_date()

    for checker in checkers:
        checker.check(target_date)
