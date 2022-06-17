pipeline {
    agent {
        docker { image 'selenium/node-chrome:latest'}
    }
    stages {
        stage('Test') {
            steps {
                sh 'google-chrome --version'
            }
        }
    }
}