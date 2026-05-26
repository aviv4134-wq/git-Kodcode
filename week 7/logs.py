import logging
"""
תרגיל 1 – נכון / לא נכון
סמן V אם הטענה נכונה, X אם לא:
.1 _X__ print ו-logging הם שקולים לחלוטין
.2 __V_ DEBUG מתאים למידע מפורט בזמן פיתוח
.3 _V__ מותר לכתוב סיסמה בלוג אם היא מוצפנת
.4 __X_ WARNING אומר שהמערכת קרסה
.5 __V_ FileHandler שומר לוגים לקובץ
stack trace גם כולל logger.exception __V_ .6
.7 _X__ כדאי להשתמש ברמת לוג אחת בלבד לפשטות

תרגיל 2 – התאמת רמת לוג
לכל תיאור, ציין את רמת הלוג המתאימה )ERROR / WARNING / INFO / DEBUG):
.1 משתמש התחבר בהצלחה: INFO
.2 קובץ קונפיגורציה לא נמצא: ERROR
.3 כניסה לפונקציה עם ערכי הפרמטרים: DEBUG
.4 מסד הנתונים לא זמין: ERROR
.5 מלאי מוצר נמוך מ5- יחידות: WARNING
.6 תהליך הזמנה הסתיים בהצלחה: INFO

תרגיל 3 – זיהוי בעיות
מצא את הבעיה בכל לוג ותקן:
# לוג א
logger.error('User logged in successfully')
logger.info('User logged in successfully')בעיה ותיקון: לא ישתמש ברמה נכונה  
# לוג ב
logger.info('Login', email, password)
logger.info('Login', email, bool(password)) בעיה ותיקון: שם פרטים אישיים בלוג 
# לוג ג
print('ERROR: payment failed')
בעיה ותיקון: שימוש בפרינט לא מסודר במקום בלוג logger.error(payment failed')


'%(asctime)s | %(levelname)s | %(name)s | %(message)s'
%(asctime)s: זמן ביצוע הפעולה מתי קרה בדיוק
%(levelname)s: רמת שם הלוג
%(name)s: שם של מי הריץ את הלוג כמו קבצים מודלים 
%(message)s: ההודעה עצמה 

"""



logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s | %(levelname)s | %(message)s')
logger = logging.getLogger(__name__)
logger.info('Application started')



def process_payment(user_id, amount):
    logger.info(f'Starting payment for user {user_id}')
    if amount <= 0:
       logger.error('ERROR: Invalid amount')
       return
    if amount > 10000:
       logger.warning('WARNING: Large transaction')
    logger.info(f'Payment of {amount} completed for user {user_id}')

#process_payment(0,0)

logger = logging.getLogger('payments')
logger.setLevel(logging.DEBUG)

formater = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s |%(message)s')

file_handler = logging.FileHandler('log.txt',encoding='utf-8')

file_handler.setFormatter(formater)
logger.addHandler(file_handler)

def add_numbers(a,b):
   logger.info('strat function')
   result = a + b
   logger.debug(f'the result is {result}')
   logger.info('the function works')
   return result

#print(add_numbers(1,2))


def read_config(filepath):
    logger.debug(f'the path {filepath}') 
    try:
        with open(filepath) as f:
            data = f.read()
        logger.info('you have read the data')
        return data
    except FileNotFoundError:
        logger.exception('error file not found')
        return None

#read_config('gdf')

from datetime import datetime
import json

def write_structured_log(level, module, message, **extra):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "level": level,
        "module": module,
        "message": message
    }
    log_entry.update(extra)
    print(json.dumps(log_entry))

#write_structured_log('INFO','logs','the massage transferd')

"""
logger.info('done')
מה חסר ואיך לשפר: לפרט יותר בהודעה מה קרה 
logger.error('failed')
מה חסר ואיך לשפר: לפרט למה  הייתה שגיאה
logger.info('user=%s', user_id)
מה טוב ומה עוד אפשר להוסיף
פירוט פעולה מה המשתמש עשה 

תרגיל 11 – חלוקת אירועים לרמות
סווג כל אירוע מהמערכת לרמת הלוג הנכונה:
• אדמין נכנס למערכת הניהול   DEBUGG
• שירות חיצוני לא מגיב ERROR
• פונקציית חישוב מס החלה לרוץ INFO
•  WARNING תעודת SSL עומדת לפוג בעוד 7 ימים
• הזמנה בוטלה על ידי לקוח INFO
• תשלום נכשל 3 פעמים ברצף ERROR

"""
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def register_user(email, password, age):
    logger.debug('starting to register process for email: %s', email)
    if age < 18:
        logger.warning('registring fail: User age %s is under the legal limit of 18', age)
        return
    logger.info('user registered with email: %s', email)

register_user('sdf','123rd',20)


import setup_logging

logger = setup_logging.get_logger('logs')
logger.info('the log transferd')



import logging
import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)s | request_id=%(request_id)s | user_id=%(user_id)s | %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

logger = logging.getLogger(__name__)

def process_request(request_id, user_id, action):
    context = {'request_id': request_id, 'user_id': user_id}
    
    logger.info('Starting action: %s', action, extra=context)
    
    logger.info('validating data ', extra=context)
    
    logger.info('finished action: %s successfully', action, extra=context)

process_request(request_id='req-101', user_id=42, action='login')
process_request(request_id='req-102', user_id=88, action='update_profile')