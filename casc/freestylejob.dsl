freeStyleJob('freestyle_casc') {
    scm {
        github('JacksonCHEN63/Django', 'master')
    }
    steps {
        shell(readFileFromWorkspace('./jenkins/test.sh'))
    }
}
