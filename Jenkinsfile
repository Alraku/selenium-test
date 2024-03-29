pipeline {
    agent any
    stages {
        stage('Start Grid') {
            steps {
                script {
                    sh 'docker start Selenium'
                    sh 'docker run -d --net grid -p 5900:5900 -e SE_EVENT_BUS_HOST=Selenium --shm-size="2g" -e SE_EVENT_BUS_PUBLISH_PORT=4442 -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 selenium/node-chrome:latest'
                    //sh 'docker run -d --net grid -p 5901:5900 -e SE_EVENT_BUS_HOST=Selenium --shm-size="2g" -e SE_EVENT_BUS_PUBLISH_PORT=4442 -e SE_EVENT_BUS_SUBSCRIBE_PORT=4443 selenium/node-edge:latest'
                }
            }
        }
        stage('Checkout') {
            steps {
                script {
                    git branch: 'main', credentialsId: 'Github', url: 'https://github.com/Alraku/Test-Automation'
                }
            }
        }
        stage('Setup Env') {
            steps {
                script {
                    sh 'pip3 --version'
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate'
                    sh 'pip3 install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // sh 'python3 -m pytest tests/unit/register_tests.py'
                    // sh 'python3 tests/unit/register_tests.py'
                    sh 'python3 -m pytest tests/unit/login_tests.py::TestLogin::test_login_valid_user'
                }
            }
        }
    }
    post {
        always {
            script {
                def doc_containers = sh(returnStdout: true, script: 'docker ps -aq --filter expose=5900/tcp').replaceAll("\n", " ") 
                if (doc_containers) {
                    sh "docker stop ${doc_containers}"
                    sh "docker container rm ${doc_containers}"
                }
                sh 'docker stop Selenium'
            }
        }
    }
}