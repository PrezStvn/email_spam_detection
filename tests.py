import unittest
import requests
import json

class TestEmailPredictionEndpoint(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://localhost:5000/predict"

    def test_predict_success(self):
        """ Test the endpoint with valid input. """
        data = {'subject': 'Meeting Reminder', 'body': 'Reminder about the meeting at 3 PM'}
        response = requests.post(self.base_url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', response.json())

    def test_empty_fields(self):
        """ Test the endpoint with empty subject and body to trigger a 400 error. """
        data = {'subject': '', 'body': ''}
        response = requests.post(self.base_url, json=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

    def test_missing_fields(self):
        """ Test the endpoint with missing subject or body to trigger a 400 error. """
        data = {'body': 'This is a test'}
        response = requests.post(self.base_url, json=data)
        self.assertEqual(response.status_code, 500)
        self.assertIn('error', response.json())

        data = {'subject': 'Test'}
        response = requests.post(self.base_url, json=data)
        self.assertEqual(response.status_code, 500)
        self.assertIn('error', response.json())

    def test_invalid_characters(self):
        """ Test the endpoint with invalid characters to trigger internal processing. """
        data = {'subject': 'Test$$$###', 'body': 'Hello###$$$'}
        response = requests.post(self.base_url, json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', response.json())

    def test_known_spam(self):
        """ Test the endpoint with a known spam email taken from the training dataset."""
        data = {'subject': 'Are Your Mortgage Rates The Best They Can Be........ 0922LkVT8-113rFxd3342c-21 ',
                'body': """-Version: 1.0 Content-Type: text/plain; charset="us-ascii" X-Priority: 3 (Normal) X-Msmail-Priority: Normal X-Mailer: Microsoft Outlook Express 5.50.4522.1200 Importance: Normal Sender: fork-admin@xent.com Errors-To: fork-admin@xent.com X-Beenthere: fork@spamassassin.taint.org X-Mailman-Version: 2.0.11 Precedence: bulk List-Help: <mailto:fork-request@xent.com?subject=help> List-Post: <mailto:fork@spamassassin.taint.org> List-Subscribe: <http://xent.com/mailman/listinfo/fork>, <mailto:fork-request@xent.com?subject=subscribe> List-Id: Friends of Rohit Khare <fork.xent.com> List-Unsubscribe: <http://xent.com/mailman/listinfo/fork>, <mailto:fork-request@xent.com?subject=unsubscribe> List-Archive: <http://xent.com/pipermail/fork/> Date: Fri, 26 Jul 0102 18:03:12 +0900 Content-Transfer-Encoding: 8bit Dear Homeowner, Interest Rates are at their lowest point in 40 years! We help you find the best rate for your situation by matching your needs with hundreds of lenders! Home Improvement, Refinance, Second Mortgage, Home Equity Loans, and much, much more! You're eligible even with less than perfect credit! This service is 100% FREE to home owners and new home buyers without any obligation. Where others say NO, we say YES!!! http://www243.wiildaccess.com Take just 2 minutes to complete the following form. There is no obligation, all information is kept strictly confidential, and you must be at least 18 years of age. Service is available within the United States only. This service is fast and free. http://www243.wiildaccess.com +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ To opt out: http://www243.wiildaccess.com/optout.html 8960ryoE6-752DjSn8958wQDd4-522UPqi8940xzrR4-094LKl46 http://xent.com/mailman/listinfo/fork
"""}
        response = requests.post(self.base_url, json=data)
        prediction = response.json()['prediction']
        expected = 'spam'
        self.assertEqual(prediction, expected)

    def test_known_ham(self):
        """ Test the endpoint with a known ham email taken from the training dataset."""
        data = {'subject': 'The Evil Gerald Online - Breaking News ',
                'body': """Wed, 26 Jun 2002 11:24:51 +0100 MIME-Version: 1.0 Content-Type: multipart/alternative; boundary="----=_NextPart_000_0007_01C21D04.16C6D7C0" X-Priority: 3 X-Msmail-Priority: Normal X-Mailer: Microsoft Outlook Express 5.00.2014.211 X-Mimeole: Produced By Microsoft MimeOLE V5.00.2014.211 This is a multi-part message in MIME format. ------=_NextPart_000_0007_01C21D04.16C6D7C0 Content-Type: text/plain; charset="iso-8859-1" Content-Transfer-Encoding: quoted-printable Get another fix of Ireland's Only Newspaper with a large dose of = Breaking News The Evil Gerald Staff ------=_NextPart_000_0007_01C21D04.16C6D7C0 Content-Type: text/html; charset="iso-8859-1" Content-Transfer-Encoding: quoted-printable <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN"> <HTML><HEAD> <META http-equiv=3DContent-Type content=3D"text/html; = charset=3Diso-8859-1"> <META content=3D"MSHTML 5.50.4916.2300" name=3DGENERATOR> <STYLE></STYLE> </HEAD> <BODY bgColor=3D#ffffff> <DIV><FONT face=3DArial size=3D2>Get another fix of <A=20 href=3D"http://www.evilgerald.com">Ireland's Only Newspaper </A>with a = large dose=20 of <A href=3D"http://www.evilgerald.com/Breaking_news.htm">Breaking=20 News</A></FONT></DIV> <DIV><FONT face=3DArial size=3D2></FONT>&nbsp;</DIV> <DIV><FONT face=3DArial size=3D2>The Evil Gerald = Staff</FONT></DIV></BODY></HTML> ------=_NextPart_000_0007_01C21D04.16C6D7C0--
"""}
        response = requests.post(self.base_url, json=data)
        prediction = response.json()['prediction']
        expected = 'spam'
        self.assertEqual(prediction, expected)

if __name__ == '__main__':
    unittest.main()