#!/usr/bin/Rscript --vanilla

# compiles all .Rmd files in _R directory into .md files in Pages directory,
# if the input file is older than the output file.

# run ./knitpages.R to update all knitr files that need to be updated.

KnitPost <- function(input, outfile, base.url="/", include.code=TRUE) {
    # this function is a modified version of an example here:
    # http://jfisher-usgs.github.com/r/2012/07/03/knitr-jekyll/
    require(knitr);
    render_jekyll()

    env = new.env()
    env$include.code = include.code
    env$fig.path = paste0("../../figs/", sub(".Rmd$", "", basename(input)), "/")
    env$base.url = base.url
    knit(input, outfile, envir = env)
}

setwd("_R")

for (infile in list.files(".", pattern="*.Rmd$")) {
    pattern = "_\\/^\\d\\d\\d\\d\\-\\d\\d\\-\\d\\d\\-"
    folder = ifelse(grepl(pattern, infile), "../posts", "../code")

    outfile = paste0(folder, "/", sub(".Rmd$", ".md", basename(infile)))

    # knit only if the input file is the last one modified
    if (!file.exists(outfile) |
        file.info(infile)$mtime > file.info(outfile)$mtime) {
        KnitPost(infile, outfile, base.url="/RData/")
        
        # also knit a code-less version
        transcript.outfile = paste0("../_transcript/raw/",
                                sub(".Rmd$", ".md", basename(infile)))
        KnitPost(infile, transcript.outfile, include.code=FALSE)
    }
}
