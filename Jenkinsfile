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
        sh 'ls -la'
        sh 'docker build -t jobportal .'
    }
}

        stage('Stop Old Container') {
            steps {
                sh 'docker rm -f jobportal-container || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh 'docker run -d -p 5000:5000 --name jobportal-container jobportal'
            }
        }
    }
}