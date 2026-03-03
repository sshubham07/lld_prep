class Fine:
    @staticmethod
    def collect_fine(member_id, days):
        amount = days * 1.0  # $1 per late day
        print(f"Collected fine of ${amount:.2f} from member {member_id}")
        return amount
