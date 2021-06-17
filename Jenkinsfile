pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                sh 'df -h'
            }
        }

        stage('Stage 2') {
            steps {
                echo 'heeee'
            }
        }
        
	stage('Stage 3') {
            steps {
                sh './../kson_Multibranch_Pipeline_master/jenkins/test.sh'
            }
        }

    }
}
