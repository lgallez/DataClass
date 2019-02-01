   alter table actor 
	add column actor_name varchar(50);

	    update actor
           set actor_name = concat(first_name, ',' ' ', last_name);

           set sql_safe_updates = 0;

        select first_name, last_name, actor_name
		  from actor;

        select last_name, first_name, actor_name
          from actor
         where
				(
				-- last_name like '%GEN%'
				--     or 
				last_name like '%LI%'
				);

		 select * from sakila.country;

         select country_id, country
           from country
		  where country
             in
				(
				'Afghanistan', 
				'Bangladesh',
				'China'
				);

    alter table actor 
     add column description blob;

    alter table actor 
	drop column description; 

	     select * from sakila.actor;

	     select last_name, count(*)
	 	   from actor
       group by last_name;

	select distinct last_name, COUNT(last_name) AS 'name_count'
		   from actor
       group by last_name 
		 having name_count >= 2;
           
         update actor
            set first_name = 'HARPO'
          where first_name = 'GROUCHO'
            and last_name  = 'WILLIAMS';
         select first_name, last_name
		   from actor
          where first_name = 'HARPO';

				show create table address;
				create table if not exists
						   `address` (
						`address_id` smallint(5) unsigned not null auto_increment,
						   `address` varchar(50) not null,
						  `address2` varchar(50) default null,
						  `district` varchar(20) not null,
						   `city_id` smallint(5) unsigned not null,
					   `postal_code` varchar(10) default null,
						     `phone` varchar(20) not null,
						  `location` geometry not null,
					   `last_update` timestamp not null default current_timestamp on update current_timestamp,
					        		 primary key (`address_id`),
									 key `idx_fk_city_id` (`city_id`),
						  			 spatial key`idx_location` (`location`),
						   			 constraint `fk_address_city` 
						 			 foreign key(`city_id`) 
						  			 references `city` (`city_id`) ON UPDATE CASCADE
									 ) 
	ENGINE=InnoDB AUTO_INCREMENT=606 DEFAULT CHARSET=utf8;

	         select staff.first_name, staff.last_name, address.address
	           from staff
         inner join address 
				 on staff.address_id = address.address_id;

			 select staff.first_name, staff.last_name, sum(payment.amount) as revenue_received
			   from staff
		 inner join payment 
				 on staff.staff_id = payment.staff_id
			  where payment.payment_date like '2005-08%'
		   group by payment.staff_id;

		     select title, count(actor_id) as actor_count
			   from film
         inner join film_actor
                 on film.film_id = film_actor.film_id
           group by title;
         
             select title, count(inventory_id) as copies_count
               from film
         inner join inventory
                 on film.film_id = inventory.film_id
              where title = 'Hunchback Impossible';
           
             select last_name,first_name, sum(amount) as total_paid
		   	   from payment
         inner join customer
                 on payment.customer_id = customer.customer_id
           group by payment.customer_id
           order by last_name asc;

			 select title 
			   from film
			  where language_id 
				 in (select language_id 
					 from language
					 where name = "english" )
				and (title like "K%") or (title like "Q%");

			 select actor_name 
			   from actor
			  where actor_id 
			     in (select actor_id
					   from film_actor
					  where film_id
					     in (select film_id from film
		                     where title = "Alone Trip"));
                                   
		  	 select first_name, last_name, email
			   from customer
	     inner join customer_list 
				 on customer.customer_id = customer_list.ID
		      where customer_list.country = 'Canada';

			 select title
			   from film
		      where film_id
				 in (select film_id 
					   from film_category
					  where category_id
						 in (select category_id
							 from category
							 where name = 'Family'));
			
			 select film.title, count(*) as rent_count 
			   from film, inventory, rental
			  where film.film_id = inventory.film_id
				and rental.inventory_id = inventory.inventory_id
		   group by inventory.film_id
		   order by count(*) desc, film.title asc;

			 select store.store_id, sum(amount) as revenue 
			   from store
         inner join staff
				 on store.store_id = staff.store_id
		 inner join payment 
				 on payment.staff_id = staff.staff_id
		   group by store.store_id;

			 select store.store_id, city.city, country.country
			   from store
         inner join address
				 on store.address_id = address.address_id
	     inner join city 
	 			 on address.city_id = city.city_id
	     inner join country 
				 on city.country_id = country.country_id;
                
		     select name, sum(payment.amount) as gross_revenue
			   from category 
	     inner join film_category 
				 on film_category.category_id = category.category_id
	     inner join inventory 
				 on inventory.film_id = film_category.film_id
	     inner join rental 
				 on rental.inventory_id = inventory.inventory_id
	     right join payment
			     on payment.rental_id = rental.rental_id
	       group by name
           order by gross_revenue desc
			  limit 5;
             
	drop view if exists top_five_genres;
		create view top_five_genres as
			 select name,sum(payment.amount) as gross_revenue
			   from category
		 inner join film_category
				 on film_category.category_id = category.category_id
		 inner join inventory
				 on inventory.film_id =  film_category.film_id
		 inner join rental
				 on rental.inventory_id = inventory.inventory_id
		 right join payment 
				 on payment.rental_id = rental.rental_id
		   group by name
		   order by gross_revenue desc
			  limit 5;

			 select * from top_five_genres;

		  drop view top_five_genres;

