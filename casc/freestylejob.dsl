freeStyleJob('freestyle_casc') {
    scm {
        github('JacksonCHEN63/Django', 'master')
    }
    steps {
      script {
        shell(readFileFromWorkspace('./jenkins/test.sh'))
      }
    }
}
