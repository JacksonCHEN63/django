multibranchPipelineJob('multibranch_github') {
    branchSources {
        github {
            id('23232323') // IMPORTANT: use a constant and unique identifier
            scanCredentialsId('github-ci')
            repoOwner('JacksonCHEN63')
            repository('Django.git')
            scanCredentialsId('df7cc8bc-aa6c-43a5-a8ba-bccaf9d5ca38')
        }
    }
}
