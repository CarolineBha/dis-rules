# Association rule-based discourse analysis (*dis-rules*)
The *dis-rules* project introduces association rule mining to discourse analysis. Compared to co-occurence approaches, the proposed approach advances the detection of clusters by reducing the bias towards highly frequent claims, thereby faciliating a better identification of discursive frames.

Parliamentary debates have been coded manually using the [Discourse Network Analyzer](https://github.com/leifeld/dna) developed by Philip Leifeld ([2016](https://books.google.co.uk/books/about/Policy_Debates_as_Dynamic_Networks.html?id=xKLuCwAAQBAJ&printsec=frontcover&source=kp_read_button&redir_esc=y#v=onepage&q&f=false)). The raw data has then been exported, cleaned and prepared for analysis in Python.

The Python code allows us to:
* Use the popular [Apriori algorithm](http://rasbt.github.io/mlxtend/user_guide/frequent_patterns/apriori/) to:
    * Generate frequent itemsets
    * Find association rules
* Generate undirected network graphs from association rules
* Compute the [Louvain modularity score](https://github.com/taynaud/python-louvain/) and global clustering coefficient
* Compute a contestedness score for each concept and an average score

### Citation
If you use the dataset(s) or code, please cite this paper:

[Bhattacharya, Caroline (2022), "Restrictive Rules of Speechmaking as a Tool to Maintain Party Unity: The Case of Oppressed Political Conflict in German Parliament Debates on the Euro Crisis", *Party Politics*, online first.](https://journals.sagepub.com/doi/full/10.1177/13540688221086226)

For comments or questions, please contact the author: https://blogs.helsinki.fi/czwerner/