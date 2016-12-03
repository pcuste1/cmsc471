#!/bin/csh -x

set Dom = *domain*.pddl

foreach f (*.pddl)

    if ( $f !~ *domain*) then

	blackbox -o $Dom -f $f -g $f.OUT

    endif

end
