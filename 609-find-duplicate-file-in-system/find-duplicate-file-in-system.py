class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        from collections import defaultdict
        content_to_paths = defaultdict(list)
        
        for path_info in paths:
            parts = path_info.split(' ')
            directory = parts[0]
            
            for file_info in parts[1:]:
                # Find the index of '(' to separate file name and content
                idx = file_info.find('(')
                file_name = file_info[:idx]
                file_content = file_info[idx + 1:-1] # Exclude closing parenthesis
                
                full_path = f"{directory}/{file_name}"
                content_to_paths[file_content].append(full_path)
                
        # Return groups that have at least two file paths
        return [paths_list for paths_list in content_to_paths.values() if len(paths_list) > 1]