pipeline {
    agent { any
    }
    stages {
        stage('Build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Compile') {
			steps {
				sh 'python add2nums.py'
			}
		}
		stage('Test') {
			steps {
				sh 'python test.py'
			}
		}
    }
}
