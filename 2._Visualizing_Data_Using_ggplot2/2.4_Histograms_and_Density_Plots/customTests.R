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
