Detect a user's activity time anomaly for the CloudTrail data.


IAM field:
userIdentity.arn

List of IAM uesrs:

"arn:aws:iam::811596193553:user/Level6": 905082,  
"arn:aws:iam::811596193553:user/backup": 915834,  
"arn:aws:iam::811596193553:root": 10997,  
"arn:aws:iam::811596193553:user/Level5": 39,  
"arn:aws:iam::811596193553:user/piper": 143,  
"arn:aws:iam::811596193553:user/SecurityMokey": 4522,  

A simple demo can be:

python3 main.py demo ./data/fea.csv

The prediction result is saved to: "result/pred_result.json"
