print('Finished after %.1f' % elapsed, 'seconds '
      'with status %s.' % status)
# %-formatting is limited as to the types it supports. 
# Only ints, strs, and doubles can be formatted.
print(f'Finished after {elapsed:.1f} seconds '
      f'with status {status}.')