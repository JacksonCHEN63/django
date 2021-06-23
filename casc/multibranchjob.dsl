multibranchPipelineJob('Multibranch_casc') {
    branchSources {
        git {
            id('123456789') // IMPORTANT: use a constant and unique identifier
            remote('https://github.com/JacksonCHEN63/Django.git')
            credentialsId('github-ci')
            includes('JENKINS-*')
        }
    }
}
