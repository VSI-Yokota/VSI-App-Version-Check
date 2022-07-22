# coding: utf-8

from checkers.acrobat import AcrobatVersionCheck
from checkers.adobe_security import AdobeSecurityVersionCheck
from checkers.android import AndroidVersionCheck
from checkers.apache import ApacheVersionCheck
from checkers.aquos import AquosVersionCheck
from checkers.aterm_wg2600hp3 import AtermWG2600HP3VersionCheck
from checkers.buffalo import TeraStationVersionCheck
from checkers.buffalo import WZR_D1100HVersionCheck
from checkers.chrome import ChromeVersionCheck
from checkers.creative_cloud import CreativeCloudVersionCheck
from checkers.cybozu import CybozuVersionCheck
from checkers.firefox import FirefoxVersionCheck
from checkers.ios import IOSVersionCheck
from checkers.jpcert import JPCertCheck
from checkers.jpcert_weekly import JPCertWeeklyCheck
from checkers.keepass import KeePassVersionCheck
from checkers.keepassxc import KeePassXCVersionCheck
from checkers.kusanagi import KusanagiVersionCheck
from checkers.modx import MODXVersionCheck
from checkers.ms365_apps import MS365AppsVersionCheck
from checkers.mysql import MySQL56VersionCheck
from checkers.mysql import MySQL57VersionCheck
from checkers.mysql import MySQL80VersionCheck
from checkers.open_ssl import OpenSSLVersionCheck
from checkers.php import PHPVersionCheck
from checkers.php_for_win import PHP4WindowsVersionCheck
from checkers.teraterm import TeraTermVersionCheck
from checkers.windows import WindowsVersionCheck
from checkers.winscp import WinSCPVersionCheck
from checkers.wordpress import WordPressJPVersionCheck
from checkers.wordpress import WordPressVersionCheck
from checkers.wordpress_security import WordPressSecurityVersionCheck
from checkers.wordpress_jp_security import WordPressJpSecurityVersionCheck
from checkers.yamaha import RTX1200VersionCheck
from checkers.yamaha import RTX1210VersionCheck
from checkers.yamaha import WXL202VersionCheck
from datetime import datetime, timedelta
from send_mail import send_mail
from logging import basicConfig, getLogger, handlers, INFO
basicConfig(
    level=INFO,
    format='%(asctime)s [%(levelname)s]: %(name)s#%(funcName)s - %(message)s (%(filename)s:%(lineno)s)',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[handlers.TimedRotatingFileHandler(
        filename='./logs/version-check-{:%Y-%m-%d}.log'.format(datetime.now()),
        encoding='utf-8',
        backupCount=7
    )],
)

logger = getLogger(__name__)
today = datetime.today()

def get_target_date():

    try:
        file = 'target_date'
        with open(file, mode='r') as f:
            str_date = f.read()

        str_date = str_date.replace("\n", "")

        with open(file, mode='w') as f:
            f.write(today.strftime('%Y-%m-%d'))

        return datetime.strptime(str_date, '%Y-%m-%d')

    except Exception as e:
        logger.error(e)

target_date = get_target_date()

checkers = (
    AcrobatVersionCheck(target_date, "https://helpx.adobe.com/acrobat/release-note/release-notes-acrobat-reader.html"),
    AdobeSecurityVersionCheck(target_date, "https://helpx.adobe.com/jp/security.html"),
    AndroidVersionCheck(target_date, "https://source.android.com/security/bulletin?hl=ja"),
    ApacheVersionCheck(target_date, "http://httpd.apache.org/"),
    AquosVersionCheck(target_date, "https://k-tai.sharp.co.jp/support/other/shm08/update/index.html"),
    AtermWG2600HP3VersionCheck(target_date, "https://www.aterm.jp/support/verup/wg2600hp3/fw.html"),
    ChromeVersionCheck(target_date, "https://chromereleases.googleblog.com/"),
    CreativeCloudVersionCheck(target_date, "https://helpx.adobe.com/creative-cloud/release-note/cc-release-notes.html"),
    CybozuVersionCheck(target_date, "https://cs.cybozu.co.jp/office10/"),
    FirefoxVersionCheck(target_date, "https://www.mozilla.org/en-US/firefox/releases/"),
    IOSVersionCheck(target_date, "https://support.apple.com/en-us/HT201222"),
    JPCertCheck(target_date, "https://www.jpcert.or.jp/at/{}.html".format(today.year)),
    JPCertWeeklyCheck(target_date, "https://www.jpcert.or.jp/wr/{}.html".format(today.year)),
    KeePassVersionCheck(target_date, "https://keepass.info/news/news_all.html"),
    KeePassXCVersionCheck(target_date, "https://keepassxc.org/blog/"),
    KusanagiVersionCheck(target_date, "https://kusanagi.tokyo/archives/"),
    MODXVersionCheck(target_date, "http://modx.jp/news/"),
    MS365AppsVersionCheck(target_date, "https://docs.microsoft.com/ja-jp/officeupdates/microsoft365-apps-security-updates"),
    # MySQL56VersionCheck(target_date, "https://dev.mysql.com/doc/relnotes/mysql/5.6/en/"),
    # MySQL57VersionCheck(target_date, "https://dev.mysql.com/doc/relnotes/mysql/5.7/en/"),
    # MySQL80VersionCheck(target_date, "https://dev.mysql.com/doc/relnotes/mysql/8.0/en/"),
    # OpenSSLVersionCheck(target_date, "https://www.openssl.org/"),
    # PHP4WindowsVersionCheck(target_date, "http://windows.php.net/download/"),
    # PHPVersionCheck(target_date, "http://php.net/"),
    RTX1200VersionCheck(target_date, "http://www.rtpro.yamaha.co.jp/RT/docs/relnote/Rev.10.01/"),
    RTX1210VersionCheck(target_date, "http://www.rtpro.yamaha.co.jp/RT/docs/relnote/Rev.14.01/"),
    TeraStationVersionCheck(target_date, "http://buffalo.jp/download/driver/hd/ts5000_fw-win.html"),
    TeraTermVersionCheck(target_date, "https://ja.osdn.net/projects/ttssh2/news/"),
    WindowsVersionCheck(target_date, "https://portal.msrc.microsoft.com/ja-jp/security-guidance"),
    WinSCPVersionCheck(target_date, "https://winscp.net/eng/news.php"),
    WordPressJPVersionCheck(target_date, "https://ja.wordpress.org/releases/"),
    WordPressJpSecurityVersionCheck(target_date, "https://ja.wordpress.org/category/security/"),
    # WordPressSecurityVersionCheck(target_date, "https://wordpress.org/news/category/security/"),
    # WordPressVersionCheck(target_date, "https://wordpress.org/releases/"),
    WXL202VersionCheck(target_date, "http://www.rtpro.yamaha.co.jp/RT/docs/relnote/ap/Rev.16.00/"),
    WZR_D1100HVersionCheck(target_date, "https://www.buffalo.jp/support/download/detail/?dl_contents_id=61636"),
)


if __name__ == '__main__':
    try:
        out_file = './check.csv'
        with open(out_file, mode='w') as f:
            f.write(",".join(("application","status","latestdate","url\n")))

            for checker in checkers:
                f.write(checker.check(target_date))
        send_mail(target_date, out_file)
    except Exception as e:
        logger.error(e)
