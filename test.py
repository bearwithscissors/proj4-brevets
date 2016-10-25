'''
Nose tests for project4

Please note, that these functions always returns east coast times in
Pacific coast format, therefore to check the intended values without passing
them to the form, we are going to roll back 8 hours to counter the roll ahead
done in each function.

In summation, the rollback is to avoid confusion when looking at the actual
output
'''

from acp_times import *
import arrow

def open_time_tester():
    '''
    Check cases for open_time
    '''
    arrow_tester = arrow.get("2017-01-01T00:00:00+00:00")
    # This line is to ensure we offset the 8 hour difference incurred
    # for ETC in the output
    arrow_tester = arrow_tester.replace(hours=-8)

    #open_time( control_dist_km, brevet_dist_km, brevet_start_time )

    #Check Fringe Cases
    output_negative = open_time( -1, 1000, str(arrow_tester) )
    assert output_negative == "2017-01-01T00:00:00+00:00"
    output_0k = open_time( 0, 1000, str(arrow_tester) )
    assert output_0k == "2017-01-01T00:00:00+00:00"

    #Check General Cases
    output_50k = open_time( 50, 1000, str(arrow_tester) )
    assert output_50k == "2017-01-01T01:28:00+00:00"
    output_100k = open_time( 100, 1000, str(arrow_tester) )
    assert output_100k == "2017-01-01T02:56:00+00:00"
    output_200k = open_time( 200, 1000, str(arrow_tester) )
    assert output_200k == "2017-01-01T05:52:00+00:00"
    output_500k = open_time( 500, 1000, str(arrow_tester) )
    assert output_500k == "2017-01-01T15:27:00+00:00"
    output_1000k = open_time( 1000, 1000, str(arrow_tester) )
    assert output_1000k == "2017-01-02T09:05:00+00:00"

    #test minutes
    arrow_tester = arrow_tester.replace(minutes=+11)
    output_50k = open_time( 50, 1000, str(arrow_tester) )
    assert output_50k == "2017-01-01T01:39:00+00:00"

def close_time_tester():
    '''
    Check cases for open_time

    note, the application input does not allow values above 1000k
    '''
    arrow_tester = arrow.get("2017-01-01T00:00:00+00:00")
    # This line is to ensure we offset the 8 hour difference incurred
    # for ETC in the output
    arrow_tester = arrow_tester.replace(hours=-8)

    #open_time( control_dist_km, brevet_dist_km, brevet_start_time )

    #Check Fringe Cases
    output_negative = close_time( -1, 1000, str(arrow_tester) )
    assert output_negative == "2017-01-01T00:00:00+00:00"
    output_0k = close_time( 0, 1000, str(arrow_tester) )
    assert output_0k == "2017-01-01T01:00:00+00:00"

    #Check General Cases
    output_50k = close_time( 50, 1000, str(arrow_tester) )
    assert output_50k == "2017-01-01T03:20:00+00:00"
    output_100k = close_time( 100, 1000, str(arrow_tester) )
    assert output_100k == "2017-01-01T06:40:00+00:00"
    output_200k = close_time( 200, 1000, str(arrow_tester) )
    assert output_200k == "2017-01-01T13:20:00+00:00"
    output_500k = close_time( 500, 1000, str(arrow_tester) )
    assert output_500k == "2017-01-02T09:20:00+00:00"
    output_1000k = close_time( 1000, 1000, str(arrow_tester) )
    assert output_1000k == "2017-01-04T03:00:00+00:00"

    #test minutes
    arrow_tester = arrow_tester.replace(minutes=+11)
    output_50k = close_time( 50, 1000, str(arrow_tester) )
    assert output_50k == "2017-01-01T03:31:00+00:00"
