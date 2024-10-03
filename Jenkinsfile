pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '/var/jenkins_home/python --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
