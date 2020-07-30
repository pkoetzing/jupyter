ax = (pd
      .pivot_table(
          df, values='New_cases', index='Date_reported', 
          columns='WHO_region', aggfunc=sum)[-30:]
      .mean()
      .plot(kind='pie'))
ax.legend()