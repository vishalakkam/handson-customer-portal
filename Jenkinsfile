pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'python -m compileall app'
            }
        }

        stage('Test') {
            steps {
                bat 'pytest'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t customer-portal:build-%BUILD_NUMBER% .'
            }
        }

        stage('Container Verification') {
    steps {
        bat 'docker run -d --name customer-portal-test -p 8081:8080 customer-portal:build-%BUILD_NUMBER%'
        bat 'curl --fail http://localhost:8081/health'
    }
}

    }
}