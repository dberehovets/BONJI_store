/* JS Document */

/******************************

[Table of Contents]

1. Vars and Inits
2. Set Header
3. Init Search
4. Init Menu
5. Init Quantity


******************************/

$(document).ready(function()
{
	"use strict";

	/*

	1. Vars and Inits

	*/

	var header = $('.header');
	var hambActive = false;
	var menuActive = false;

	setHeader();

	$(window).on('resize', function()
	{
		setHeader();
	});

	$(document).on('scroll', function()
	{
		setHeader();
	});

	initSearch();
	initMenu();
	initQuantity();
	initDelivery();

	/*

	2. Set Header

	*/

	function setHeader()
	{
		if($(window).scrollTop() > 100)
		{
			header.addClass('scrolled');
		}
		else
		{
			header.removeClass('scrolled');
		}
	}

	/*

	3. Init Search

	*/

	function initSearch()
	{
		if($('.search').length && $('.search_panel').length)
		{
			var search = $('.search');
			var panel = $('.search_panel');

			search.on('click', function()
			{
				panel.toggleClass('active');
			});
		}
	}

	/*

	4. Init Menu

	*/

	function initMenu()
	{
		if($('.hamburger').length)
		{
			var hamb = $('.hamburger');

			hamb.on('click', function(event)
			{
				event.stopPropagation();

				if(!menuActive)
				{
					openMenu();

					$(document).one('click', function cls(e)
					{
						if($(e.target).hasClass('menu_mm'))
						{
							$(document).one('click', cls);
						}
						else
						{
							closeMenu();
						}
					});
				}
				else
				{
					$('.menu').removeClass('active');
					menuActive = false;
				}
			});

			//Handle page menu
			if($('.page_menu_item').length)
			{
				var items = $('.page_menu_item');
				items.each(function()
				{
					var item = $(this);

					item.on('click', function(evt)
					{
						if(item.hasClass('has-children'))
						{
							evt.preventDefault();
							evt.stopPropagation();
							var subItem = item.find('> ul');
						    if(subItem.hasClass('active'))
						    {
						    	subItem.toggleClass('active');
								TweenMax.to(subItem, 0.3, {height:0});
						    }
						    else
						    {
						    	subItem.toggleClass('active');
						    	TweenMax.set(subItem, {height:"auto"});
								TweenMax.from(subItem, 0.3, {height:0});
						    }
						}
						else
						{
							evt.stopPropagation();
						}
					});
				});
			}
		}
	}

	function openMenu()
	{
		var fs = $('.menu');
		fs.addClass('active');
		hambActive = true;
		menuActive = true;
	}

	function closeMenu()
	{
		var fs = $('.menu');
		fs.removeClass('active');
		hambActive = false;
		menuActive = false;
	}

	/*

	5. Init Quantity

	*/

	function initQuantity()
	{
		// Handle product quantity input
		if($('.product_quantity').length)
		{
			var inputs = $('.quantity_input');
			var incButtons = $('.quantity_inc.quantity_control');
			var decButtons = $('.quantity_dec.quantity_control');

			var originalVal;
			var endVal;

			for (var i = 0; i < inputs.length; i++) {
				incButtons[i].addEventListener('click', function()
				{
					originalVal = inputs[incButtons.index(this)].value;
					endVal = parseFloat(originalVal) + 1;
					inputs[incButtons.index(this)].value = endVal;
				});

				decButtons[i].addEventListener('click', function()
				{
					originalVal = inputs[decButtons.index(this)].value;
					if(originalVal > 0)
					{
						endVal = parseFloat(originalVal) - 1;
						inputs[decButtons.index(this)].value = endVal;
					}
				});
			}

		}
	}

	function initDelivery()
	{
		var fast_del = $("#fast_delivery")
		var common_del = $("#common_delivery")
		var free_del = $("#free_delivery")
		var shipping_price = $("#shipping_price")

		var subtotal_price = parseFloat($("#subtotal_price").text().replace("$", ""))

		if (subtotal_price > 100) {
			$("#common_delivery_price").text("$0")
		}

		var common_del_price = parseFloat($("#common_delivery_price").text().replace("$", ""))
		var total_price = $("#total_price")



		fast_del.on('click', function(){
			total_price.text("$" + (subtotal_price + 4.99))
			shipping_price.text("$" + 4.99)
		})
		common_del.on('click', function(){
			total_price.text("$" + (subtotal_price + common_del_price))
			shipping_price.text("$" + common_del_price)
		})
		free_del.on('click', function(){
			total_price.text("$" + subtotal_price)
			shipping_price.text("$0")
		})
	}

});
