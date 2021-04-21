pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('hello') {
            steps {
                sh 'python --version'
            }
        }
    }
}
