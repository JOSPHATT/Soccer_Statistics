import pandas as pd

def preprocess_data(df):
    try:
        # Data preparation
        df = df.drop_duplicates()
        df_numeric = df.select_dtypes(include=['float64', 'int64'])
        df[df_numeric.columns] = df_numeric.fillna(df_numeric.median())
        df_categorical = df.select_dtypes(include=['object'])
        for col in df_categorical.columns:
            df[col] = df[col].fillna(df[col].mode()[0])

        if 'H_GOALS' in df.columns and 'A_GOALS' in df.columns:
            df['home_team_goal'] = df['H_GOALS']
            df['away_team_goal'] = df['A_GOALS']
        return df
    except Exception as e:
        print(f"Error during data preparation: {e}")
        raise e


def process_team_statistics(df):
    try:
        # Process home data
        home_df = df[['HOME', 'home_team_goal', 'away_team_goal']].copy()
        home_df.columns = ['TEAM', 'goals_for', 'goals_against']
        home_df['matches_played'] = 1
        home_df['matches_won'] = (home_df['goals_for'] > home_df['goals_against']).astype(int)
        home_df['matches_drawn'] = (home_df['goals_for'] == home_df['goals_against']).astype(int)
        home_df['matches_lost'] = (home_df['goals_for'] < home_df['goals_against']).astype(int)

        # Process away data
        away_df = df[['AWAY', 'away_team_goal', 'home_team_goal']].copy()
        away_df.columns = ['TEAM', 'goals_for', 'goals_against']
        away_df['matches_played'] = 1
        away_df['matches_won'] = (away_df['goals_for'] > away_df['goals_against']).astype(int)
        away_df['matches_drawn'] = (away_df['goals_for'] == away_df['goals_against']).astype(int)
        away_df['matches_lost'] = (away_df['goals_for'] < away_df['goals_against']).astype(int)

        # Combine home and away data
        team_df = pd.concat([home_df, away_df])
        team_stats = team_df.groupby('TEAM').sum().reset_index()
        team_stats['goal_difference'] = team_stats['goals_for'] - team_stats['goals_against']
        team_stats['goals_scored_per_match'] = team_stats['goals_for'] / team_stats['matches_played']
        team_stats['goals_conceded_per_match'] = team_stats['goals_against'] / team_stats['matches_played']
        team_stats['goal_difference_per_match'] = team_stats['goal_difference'] / team_stats['matches_played']
        team_stats['win_rate'] = (team_stats['matches_won'] / team_stats['matches_played']) * 100
        team_stats['draw_rate'] = (team_stats['matches_drawn'] / team_stats['matches_played']) * 100
        team_stats['loss_rate'] = (team_stats['matches_lost'] / team_stats['matches_played']) * 100
        team_stats['scoring_strength'] = team_stats['goals_scored_per_match'] + (0.5 * team_stats['goal_difference_per_match'])
        return team_stats
    except Exception as e:
        print(f"Error during data processing: {e}")
        raise e