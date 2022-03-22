import boto3
from flask import Flask, render_template

app = Flask(__name__)
ec2_client = boto3.client('ec2')

def list_vpcs():
    response = ec2_client.describe_vpcs()
    return response['Vpcs']

@app.route('/',methods=['GET'])
def home():

    return render_template(
        'index.html',
        rgb = 'rgb(237, 233, 9)'
    )

if __name__ == "__main__":
    app.run(debug=True)