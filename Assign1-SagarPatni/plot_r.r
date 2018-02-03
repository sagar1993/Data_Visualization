p <- ggplot(winner, aes(double, secPointWon ,colour=factor(win), label=player, size=return, group=year))
p + 
  geom_point() + theme_bw() +
  labs(title = "Trends from Australian Open Championship matches", x = "Double fault", y = "Sec. Points Won", color = "Win") +
  geom_text(size=5, vjust=0.1, hjust="inward", position = position_jitter(width=5, height=1.5)) + geom_line(size=1) + facet_wrap(~year)

