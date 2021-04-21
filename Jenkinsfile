pipeline {
    agent { docker { image 'python:3.5.1' } }
    stages {
        stage('Build') {
            steps {
                sh 'python --version'
            }
        }
		stage('Run') {
			steps {
				sh 'python first.py'
			}
		}
    }
}
