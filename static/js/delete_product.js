$(document).ready(() => {

    console.log('delete_product.js -> Start');


    $('#delete-all').on('click', '.delete-all-btn', (event) => {
        // 1

        console.log('delete-all -> Click');
        // 2

        const userId = $('#user-id').val();
        console.log('userId -> ' + userId);

        // 4
        let orderId = $('#order-id-all').val();
        console.log('orderId -> ' + orderId);

        $.ajax({
                url : '/orders/order_delete_all',
                data: `oid=${orderId}&uid=${userId}`,
        });
    });


    $('#delete-product').on('click', '.delete-product-btn', (event) => {
        // 1

        console.log('delete-product-btn -> Click');
        // 2

        const userId = $('#user-id').val();
        console.log('userId -> ' + userId);

        // 4
        let orderId = $('#order-id').val();
        console.log('orderId -> ' + orderId);

        $.ajax({
                url : '/orders/order_delete',
                data: `oid=${orderId}&uid=${userId}`,
        });
    });
});