import config
import mytools
import datetime
import os

basedir = '\\\\ipc-vfs01\\SEC$\\SEC Examination Information Request List 2017\\Independent Portfolio Consultants, Inc. Request'
mytools.general().make_sure_path_exists(basedir)
dirlist = [
    '01. Adviser organization chart ',
    '02. List of current employees',
    '03. List of any of the Advisers employees',
    '04. List of any former employees & complaints ',
    '05. Threatened, pending and settled litigation',
    '06. List of any sub-advisers.',
    '07. The Form ADV Part 2 ',
    '08. Client advisory contracts or agreements',
    '09. Current fee schedule',
    '10. A list of all committees ',
    '11. Names of any joint ventures',
    '12. Key service providers',
    '13. Compliance policies and procedures',
    '14. Annual review, recently completed',
    '15. Compliance risks, policies and changes',
    '16. Complaints & process used for monitoring',
    '17. Non-compliance Record',
    '18. Client Information',
    '18a. Data',
    '18b. Clients lost',
    '18c. Other advisory clients not named ',
    '19. Pitch books',
    '20. Advertisements ',
    '21. Accounting Statements',
    '22. List of investors debt & equity instruments',
    '23. Documents for loans or promissory notes',
    '24. List fee splitting or revenue sharing arrangements',
]

for d in dirlist:
    full_path = os.path.join(basedir, d)
    mytools.general().make_sure_path_exists(full_path)
    print full_path

basedir = '\\\\ipc-vfs01\\SEC$\\SEC Examination Information Request List 2017\\Blue Shores Capital request'
mytools.general().make_sure_path_exists(basedir)
dirlist = [
    '01. Adviser organization chart ',
'02. List of current employees',
'03. List of any of the Advisers employees',
'04. List of any former employees & complaints ',
'05. Threatened, pending & settled litigation',
'06. List of any sub-advisers',
'07. Form ADV Part 2 ',
'08. Client advisory contracts or agreements',
'09. A list of all committees ',
'10. Names of any joint ventures',
'11. Key service providers',
'12. Compliance policies & procedures',
'13. Annual review, recently completed',
'14. Compliance risks, policies & changes',
'15. Complaints & process used for monitoring',
'16. Non-compliance Record',
'17. Trade Blotter',
'18. Client Information',
'18a. Data',
'18b. Clients lost',
'18c. Other advisory clients not named ',
'19. Broker Dealer Affiliations',
'20. Pitch Books',
'21. Advertisements ',
'22. Accounting Statements',
'23. List of investors in any debt or equity instruments',
'24. Documents for loans or promissory notes',
'25. List fee splitting or revenue sharing arrangements',
'26. For each private fund',
'26a. Private placement offering memor&a',
'26b. Limited partnership operating agreement',
'26c. Investment management advisory agreement',
'26d. Subscription agreements',
'26e. Side letters',
'27. For each private fund names of current investors ',
'28. For each private fund documents concerning subscriptions & redemptions',
'29. Lis of solicitors, consultants, placement agents',
]

for d in dirlist:
    full_path = os.path.join(basedir, d)
    mytools.general().make_sure_path_exists(full_path)
    print full_path

basedir = '\\\\ipc-vfs01\\SEC$\\SEC Examination Information Request List 2017\\IPC Private Wealth Request'
mytools.general().make_sure_path_exists(basedir)
dirlist = [
'01. Organization chart '	,
'02. List of current employees'	,
'03. List of resigned or terminated & reason'	,
'04. Resigned or terminated alleging potential violations of securities laws '	,
'05. A list of all offices '	,
'06. Any threatened, pending and settled litigation '	,
'07. List of sub-advisers.'	,
'08. Form ADV Part 2'	,
'09. All forms of client advisory contracts '	,
'10. List committees '	,
'11. Names of any joint ventures '	,
'12. Key service providers'	,
'13. Compliance policies and procedures'	,
'14. Annual review of its policies and'	,
'15. Inventory of compliance risks '	,
'16. Complaints and information about the monitoring process'	,
'17. Any non-compliance '	,
'18. A trade blotter '	,
'19. Clients Information'	,
'19A. Data'	,
'19B. Clients lost'	,
'19C. Clients not named'	,
'20. Affiliated broker-dealers'	,
'21. Pitch books'	,
'22. Advertisements '	,
'23. Accounting'	,
'24. List of all investors '	,
'25. Client who made a loan to the Adviser'	,
'26. List all fee splitting or revenue sharing arrangements'	,
'27. Solicitor consultant placement agents'	,
]

for d in dirlist:
    full_path = os.path.join(basedir, d)
    mytools.general().make_sure_path_exists(full_path)
    print full_path
