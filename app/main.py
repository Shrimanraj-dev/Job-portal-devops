from flask import Flask, render_template, request
import boto3
import uuid
REGION = 'ap-south-1'  

app = Flask(__name__)
dynamodb = boto3.resource('dynamodb', region_name=REGION)
s3 = boto3.client('s3', region_name=REGION)
sns = boto3.client('sns', region_name=REGION)

TABLE_NAME = 'Applications'
BUCKET_NAME = 'job-application-resumesproject11807'
TOPIC_ARN = 'arn:aws:sns:ap-south-1:845488705635:job-application-topic'

@app.route('/', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        resume = request.files['resume']
        app_id = str(uuid.uuid4())

        # Upload resume to S3
        s3.upload_fileobj(resume, BUCKET_NAME, f"{app_id}-{resume.filename}")

        # Store to DynamoDB
        table = dynamodb.Table(TABLE_NAME)
        table.put_item(Item={
            'application_id': app_id,
            'name': name,
            'email': email,
            'resume_key': f"{app_id}-{resume.filename}"
        })

        # Send SNS notification
        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject='New Job Application',
            Message=f"New application from {name} ({email})"
        )

        return "Application submitted successfully!"
    return render_template('form.html')
app.run(host='0.0.0.0',port=80)

