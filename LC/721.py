class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        def partial_merge_sets(dict_sets):
            for i in dict_sets.keys():
                for j in dict_sets.keys():
                    if i == j:
                        break
                    int_set = dict_sets[i].intersection(dict_sets[j])
                    if len(int_set) > 0:
                        dict_sets[i] = dict_sets[i].union(dict_sets[j])
                        del dict_sets[j]
                        return True, dict_sets
            return False, dict_sets
                        
        # this will contain names as they key and value as dict with the accounts
        # e.g. accounts dict
        # {
        #     "John" : {
        #         0 : set("johnsmith@mail.com","john_newyork@mail.com"),
        #         1 : set("johnsmith@mail.com","john00@mail.com"),
        #         2 : set("johnnybravo@mail.com")
        #     },
        #     "Mary" : {
        #         0 : set("mary@mail.com")
        #     }
        # }
        accounts_dict = {}
        # iterate through the original values and create the account dict
        for acc in accounts:
            account_name = acc[0] # get the name
            account_emails_set = set(acc[1:]) # get the emails as sets
            if account_name in accounts_dict:
                part_dict = accounts_dict[account_name]
                part_dict[len(part_dict)] = account_emails_set
            else:
                part_dict = {0: account_emails_set}
                accounts_dict[account_name] = part_dict

        # merge the accounts
        for account_name, account_email_dict in accounts_dict.items():
            # keep merging until they are no possible merges
            while(True):
                flag, account_email_dict = partial_merge_sets(account_email_dict)
                if flag == False:
                    break

        # return sorted results
        final_result = []
        for account_name, account_email_dict in accounts_dict.items():
            for key, val in account_email_dict.items():
                final_result.append([account_name]+sorted(list(val)))
            
        return final_result