print('The number of Corona deaths in the first half of this year for Sweden was ',
      df2.loc[('2020-06-30', 'Sweden'), 'Cumulative_deaths'].values[0], '.', sep='')