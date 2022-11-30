class Match:
  def __init__(self, home_team, away_team, date_time, stadium_id, match_id):
    self.home_team = home_team
    self.away_team = away_team
    self.date_time = date_time
    self.stadium_id = stadium_id
    self.match_id = match_id
    self.taken_seats = []
    self.general_clients = 0
    self.VIP_clients = 0
    self.sold_tickets = 0
    self.attendance = 0
    self.total_spent = 0


    
  def show_match(self):
    print(f'''
      ID: {self.match_id}
      Home Team: {self.home_team}
      Away Team: {self.away_team}
      Date & Time: {self.date_time}
      Stadium: {self.stadium_id} 
      '''
    )
