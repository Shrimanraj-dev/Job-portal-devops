pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/Shrimanraj-dev/Job-portal-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t jobportal .'
            }
        }

        stage('Stop Old Container') {
            steps {
                bat 'docker rm -f jobportal-container || exit 0'
            }
        }

        stage('Run New Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name jobportal-container jobportal'
            }
        }
    }
}
