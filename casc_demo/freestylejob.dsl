freeStyleJob('demo/freestyle_casc') {
    scm {
        github('JacksonCHEN63/Django', 'master')
    }
    steps {
        shell 'echo "hi"'
        shell 'sh jenkins/test.sh'
    }
}
