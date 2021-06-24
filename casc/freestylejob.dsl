freeStyleJob('freestyle_casc') {
    scm {
        github('JacksonCHEN63/Django', 'master')
    }
    steps {
      script {
        sh "jenkins/test.sh"
      }
    }
}
