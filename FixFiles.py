3
��]S  �               @   s    d dl Z G dd� d�Ze�  dS )�    Nc               @   s$   e Zd Zdd� Zdd� Zdd� ZdS )�
RenameFilec             C   s*   t d�}t d�}t d�}| j|||� d S )Nzpath : zInput : z	Output : )�input�rename)�self�path�Input�Output� r	   �1/mnt/c/Users/IIII/Desktop/V7x-Fishing/FixFiles.py�__init__   s    zRenameFile.__init__c             C   sN   g }t jj|�}x8t j|�D ]*\}}}x|D ]}|j|d | � q,W qW |S )N�/)�osr   �join�walk�append)r   �Path�filesr   �d�r�f�Fr	   r	   r
   �Files
   s    
zRenameFile.Filesc             C   sZ   xT| j |�D ]F}|j|�dkrtd| � tj||j||�� td|j||� � qW d S )N�   z
[1;32mz[1;36m�����)r   �find�printr   r   �replace)r   r   r   r   �ir	   r	   r
   r      s    
zRenameFile.renameN)�__name__�
__module__�__qualname__r   r   r   r	   r	   r	   r
   r      s   	r   )r   r   r	   r	   r	   r
   �<module>   s   #