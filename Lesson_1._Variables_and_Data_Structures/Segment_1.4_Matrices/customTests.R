# Put custom tests in this file.

#' Test that the ggplot object created by the expression matches the given
#' aesthetics
#' 
#' @family AnswerTests
aes_matches <- function(...) {
	e <- get("e", parent.frame())
	desired = list(...)

	v = e$val
	if (!all(class(v) == c("gg", "ggplot"))) {
	    return(FALSE)
	}

	if (length(v$mapping) != length(desired)) {
	    return(FALSE)
	}

	for (a in names(desired)) {
		if (desired[[a]] != v$mapping[[a]]) {
			return(FALSE)
		}
	}
	return(TRUE)
}

#' Test that the user's value is identical to a given data.table
#' 
#' @family AnswerTests
dt_matches <- function(nr=NULL, nc=NULL, col.names=NULL) {
	e <- get("e", parent.frame())

    # basic dimensions
    if (!is.data.table(e$val)) {
        return(FALSE)
    }
    if (!is.null(nr) && nrow(e$val) != nr) {
        return(FALSE)
    }
    if (!is.null(nc) && ncol(e$val) != nc) {
        return(FALSE)
    }

    # column names
    if (!is.null(col.names) && !all(col.names == colnames(e$val))) {
        return(FALSE)
    }

    # that's all for now
    return(TRUE)
}
