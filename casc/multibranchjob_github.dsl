multibranchPipelineJob('multibranch_github') {
    branchSources {
        github {
            id('23232323') // IMPORTANT: use a constant and unique identifier
            scanCredentialsId('github-ci')
            repoOwner('JacksonCHEN63')
            repository('Django.git')
            scanCredentialsId(c2233ae8-1ed7-480d-9a13-cf33fcb5989c)
        }
    }
}
